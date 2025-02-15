from bottle import route, run, template, static_file, TEMPLATE_PATH
import os
import yaml

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__), "template"))

DEFAULT_CONFIG = {
    'site-name': 'simple-docker-lander',
    'link-mode': 'default',
    'links': [
        {'name': 'Service 1', 'href': 'https://www.google.com/'},
        {'name': 'Service 2', 'href': 'https://www.reddit.com/'},
    ]
}

if __name__ == '__main__':
    config_env_var = yaml.safe_load(os.environ.get('CONFIG', '')) or {}

    # Merge the default config with the env config
    config = DEFAULT_CONFIG.copy()
    config.update(config_env_var)

    groups = [
        {'name': 'default', 'links': []}
    ]
    groups_index_map = {'default': 0}
    for link in config['links']:
        if 'group' in link:
            if link['group'] in groups_index_map:
                groups[groups_index_map[link['group']]]['links'].append(link)
            else:
                groups_index_map[link['group']] = len(groups)
                groups.append({
                    'name': link['group'],
                    'links': [link]
                })
        else:
            groups[0]['links'].append(link)

    @route('/')
    def index():
        return template("template", config=config, groups=groups)
    
    @route('/template/<filename>')
    def serve_template(filename):
        return static_file(filename, root="./template")

    run(
        server='paste',
        host='0.0.0.0',
        port='80'
    )
