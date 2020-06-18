from concurrent.futures import ProcessPoolExecutor

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=8) as  executor:
        executor.submit()