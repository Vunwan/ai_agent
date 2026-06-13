# main.py

import os
import argparse
import time

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import call_function, function_map, available_functions


def generate_content(client: genai.Client, messages: list[types.Content]):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            tools=[available_functions],
            temperature=0
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Code Assistant")
    parser.add_argument("user_prompt", type=str)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY environment variable not set")

    client = genai.Client(api_key=api_key)

    # Initial user message
    messages: list[types.Content] = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)]
        )
    ]

    MAX_ITERATIONS = 20

    for iteration in range(MAX_ITERATIONS):
        if args.verbose:
            print(f"\n--- Iteration {iteration + 1} ---")

        # -----------------------
        # Call Gemini API
        # -----------------------
        try:
            response = generate_content(client, messages)
        except Exception as e:
            print(f"Error calling Gemini API: {e}")
            return

        if not response or not response.candidates:
            print("Error: Gemini returned no candidates")
            return

        candidate_content = response.candidates[0].content
        if candidate_content is None:
            print("Error: Candidate content is None")
            return

        # -----------------------
        # Append model's response to conversation
        # -----------------------
        messages.append(types.Content(role="assistant", parts=candidate_content.parts))

        # -----------------------
        # Extract function calls
        # -----------------------
        function_calls = [
            part.function_call
            for part in candidate_content.parts
            if hasattr(part, "function_call") and part.function_call is not None
        ]

        if not function_calls:
            # No more function calls: final response
            print("\nFinal response:")
            print(response.text)
            return

        # -----------------------
        # Execute functions and collect results
        # -----------------------
        function_responses = []
        for function_call_obj in function_calls:
            result_content = call_function(function_call_obj, verbose=args.verbose)
            function_responses.extend(result_content.parts)

        # Append function results to conversation so model sees them in next iteration
        messages.append(types.Content(role="user", parts=function_responses))

    # -----------------------
    # Max iterations reached
    # -----------------------
    print("Error: maximum iterations reached without final response")
    exit(1)


if __name__ == "__main__":
    main()