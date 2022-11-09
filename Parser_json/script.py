import pandas as pd


def load_json(file_name):
    data = pd.read_json(file_name)
    my_list = []
    for item in data['items']:
        cluster_name = item['Cluster']['name']
        service_name = item['service_name']
        for configuration_item in item['configuration']:
            config_version = configuration_item['version']
            prop_protocol = configuration_item['properties']['protocol']
            prop_host = configuration_item['properties']['host']
            prop_port = configuration_item['properties']['port']
            my_list.append({
                'cluster_name': cluster_name,
                'service_name': service_name,
                'configuration_version': config_version,
                'url': '{}://{}:{}/'.format(prop_protocol, prop_host, prop_port)
            })
    return my_list


def save_excel(_name_xlsx, _data1):
    df = pd.DataFrame(_data1)
    df.rename(columns={'cluster_name': 'Имя кластера', 'service_name': 'Имя сервера',
                       'configuration_version': 'Версия конфигурации', 'url': 'Url на сервис'}, inplace=True)
    df.to_excel(_name_xlsx, sheet_name='Clusters', index=False)


if __name__ == '__main__':
    data1 = load_json('loki_links.json')
    data2 = load_json('thor_links.json')
    data1.extend(data2)
    name_xlsx: str = 'clusters.xlsx'
    save_excel(name_xlsx, data1)
