from src.bloom_filter import BloomFilter

def load_breached_passwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def build_filter(data_file):
    passwords = load_breached_passwords(data_file)
    n = len(passwords) or 1
    p = 0.01  # desired false positive probability
    bloom = BloomFilter(n, p)
    for pwd in passwords:
        bloom.add(pwd)
    return bloom
