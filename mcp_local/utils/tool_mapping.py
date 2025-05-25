from utils.search_paper import search_papers
from utils.extract_info import extract_infos

def execute_tool(tool_name, tool_args):
    mapping_tool_function = {
        "search_papers": search_papers,
        "extract_info": extract_infos
    }

    result = mapping_tool_function[tool_name](**tool_args)

    if result is None:
        result = "The operation completed but didn't return any results."

    elif isinstance(result, list):
        result = ', '.join(result)

    elif isinstance(result, dict):
        # Convert dictionaries to formatted JSON strings
        result = json.dumps(result, indent=2)

    else:
        # For any other type, convert using str()
        result = str(result)
    return result