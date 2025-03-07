import asyncio
import shutil
import argparse
import logging
from pathlib import Path

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def copy_file(file_path: Path, output_folder: Path):
    """Асинхронно копіює файл у відповідну підпапку за розширенням."""
    try:
        ext = file_path.suffix.lower().strip('.') or 'no_extension'
        dest_folder = output_folder / ext
        dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / file_path.name

        loop = asyncio.get_running_loop()
        await loop.run_in_executor(None, shutil.copy2, file_path, dest_path)
        logging.info(f'Копіювано: {file_path} -> {dest_path}')
    except Exception as e:
        logging.error(f'Помилка копіювання {file_path}: {e}')


async def read_folder(initial_folder: Path, output_folder: Path):
    """Асинхронно читає всі файли у вихідній директорії та її підпапках."""
    tasks = []
    for file_path in initial_folder.rglob('*'):
        if file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Асинхронне сортування файлів за розширеннями.')
    parser.add_argument('source', type=str, help='Вихідна папка')
    parser.add_argument('output', type=str, help='Цільова папка')
    args = parser.parse_args()

    source_folder = Path(args.source)
    destination_folder = Path(args.output)

    if not source_folder.exists() or not source_folder.is_dir():
        logging.error('Вихідна папка не існує або не є директорією.')
    else:
        asyncio.run(read_folder(source_folder, destination_folder))