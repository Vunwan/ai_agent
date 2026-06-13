import os
from google.genai import types


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)

        target_dir = os.path.normpath(
            os.path.join(working_dir_abs, directory)
        )

        # Security check: must stay inside working directory
        if os.path.commonpath([working_dir_abs, target_dir]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        # Must be a directory
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        items = os.listdir(target_dir)

        lines = []
        for item in items:
            item_path = os.path.join(target_dir, item)

            is_dir = os.path.isdir(item_path)
            size = os.path.getsize(item_path) if not is_dir else 0

            lines.append(
                f"- {item}: file_size={size} bytes, is_dir={is_dir}"
            )

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"


# ✅ Function declaration (LLM schema)
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is '.')",
            ),
        },
    ),
)