import os

# 1. Настройки фильтрации
IGNORE_DIRS = {
    '.git',
    '.idea',
    '.gradle',
    'build',
    '.kotlin',
    '.venv',
    'venv',
    '__pycache__',
    'iosApp',
}

IGNORE_FILES = {
    '.DS_Store',
    'local.properties',
    'project_to_md.py',         # исключаем сам скрипт
    'project_codebase_dump.md',  # исключаем выходной файл
}

ALLOWED_EXTENSIONS = {
    '.kt',
    '.kts',
    '.py',
    '.xml',
    '.json',
    '.gradle',
}

OUTPUT_FILE = 'project_News_codebase.md'


def get_lang_by_ext(ext):
    mapping = {
        '.kt': 'kotlin',
        '.kts': 'kotlin',
        '.py': 'python',
        '.xml': 'xml',
        '.json': 'json',
        '.gradle': 'groovy',
    }
    return mapping.get(ext.lower(), '')


def should_ignore_dir(dirname):
    return dirname in IGNORE_DIRS or dirname.startswith('.')


def should_process_file(filename):
    _, ext = os.path.splitext(filename)
    return ext.lower() in ALLOWED_EXTENSIONS and filename not in IGNORE_FILES


def dump_codebase(root_dir, output_path):
    with open(output_path, 'w', encoding='utf-8') as out_f:
        out_f.write("# Project News Codebase\n\n")

        for root, dirs, files in os.walk(root_dir):
            dirs[:] = [d for d in dirs if not should_ignore_dir(d)]

            for file in files:
                if should_process_file(file):
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, root_dir)
                    _, ext = os.path.splitext(file)
                    lang = get_lang_by_ext(ext)

                    # Записываем заголовок в Markdown
                    out_f.write(f'### File: `{relative_path}`\n\n')
                    out_f.write(f'```{lang}\n')
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as in_f:
                            out_f.write(in_f.read())
                    except Exception as e:
                        out_f.write(f'[Error reading file: {e}]')

                    out_f.write('\n```\n\n---\n\n')

    print(f'Готово! Дамп сохранен в Markdown-файл: {output_path}')


if __name__ == '__main__':
    current_dir = os.getcwd()
    dump_codebase(current_dir, OUTPUT_FILE)