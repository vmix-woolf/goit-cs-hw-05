import asyncio
import aioshutil
import argparse
import logging
from aiopath import AsyncPath

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def copy_file(file_path: AsyncPath, output_folder: AsyncPath):
    """Асинхронно копіює файл у відповідну підпапку за розширенням."""
    try:
        ext = file_path.suffix.lower().strip('.') or 'no_extension'
        dest_folder = output_folder / ext
        await dest_folder.mkdir(parents=True, exist_ok=True)
        dest_path = dest_folder / file_path.name

        await aioshutil.copy(file_path, dest_path)
        logging.info(f'Копіювано: {file_path} -> {dest_path}')
    except Exception as e:
        logging.error(f'Помилка копіювання {file_path}: {e}')


async def read_folder(initial_folder: AsyncPath, output_folder: AsyncPath):
    """Асинхронно читає всі файли у вихідній директорії та її підпапках."""
    tasks = []
    async for file_path in source_folder.glob('**/*'):
        if await file_path.is_file():
            tasks.append(copy_file(file_path, output_folder))

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Асинхронне сортування файлів за розширеннями.')
    parser.add_argument('source', type=str, help='Вихідна папка')
    parser.add_argument('output', type=str, help='Цільова папка')
    args = parser.parse_args()

    source_folder = AsyncPath(args.source)
    destination_folder = AsyncPath(args.output)

    asyncio.run(read_folder(source_folder, destination_folder))