import yaml

def get_testcase_yaml(file_path):
    with open(file_path, encoding='utf-8') as f:
        raw_data = yaml.safe_load(f)
        return [
            (item['baseInfo'],
             item['testCase'][0] if isinstance(item['testCase'], list) else item['testCase'])
            for item in raw_data
        ]
