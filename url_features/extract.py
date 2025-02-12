import re
from urllib.parse import urlparse
import tldextract

# Function to check if a URL contains an IP address
def has_ip_address(url):
    ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
    return int(bool(re.search(ip_pattern, url)))

# Function to count special characters in the URL
def count_special_chars(url):
    special_chars = ['@', '-', '_', '?', '=', '&', '%', '.', '#', '+', '$', ',', ';']
    return sum(url.count(char) for char in special_chars)

# Function to extract URL features
def extract_features(url):
    parsed_url = urlparse(url)
    domain_info = tldextract.extract(url)

    features = {
        'url_length': len(url), 
        'domain_length': len(domain_info.domain),
        'num_dots': url.count('.'),
        'num_hyphens': url.count('-'),
        'num_underscores': url.count('_'),
        'num_slashes': url.count('/'),
        'num_question_marks': url.count('?'),
        'num_equals': url.count('='),
        'num_ats': url.count('@'),
        'num_and': url.count('&'),
        'num_percent': url.count('%'),
        'num_hashes': url.count('#'),
        'num_special_chars': count_special_chars(url),
        'has_ip_address': has_ip_address(url),
        'is_https': int(parsed_url.scheme == 'https'),
        'num_subdomains': len(domain_info.subdomain.split('.')) if domain_info.subdomain else 0,
    }
    return features
