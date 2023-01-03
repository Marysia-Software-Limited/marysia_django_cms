from beret_utils import get_config, EnvValue, join_path_value, format_string
from beret_utils import get_dir

get_path = get_dir(depth=1)

DEFAULT_CONFIG = (
    # ('ONE', 1, int),
    # ('TWO', 2, int),
    # ('THREE', 3, int),
    # ('TWO_AGAIN', EnvValue('TWO'), int),
    # ('VALUE', 'default_value'),
    # ('DIR', 'test', get_path),
    # ('DIR_BIS', 'test', get_path),
    # ('SUBDIR', 'parent', join_path_value('DIR')),
    # ('SUBDIR_ENV_VALUE', EnvValue('VALUE'), join_path_value('SUBDIR')),
    # ('FILE', 'file', join_path_value('SUBDIR')),
    # ('FORMAT_STRING', "{ONE} {TWO} {THREE} {TWO_AGAIN} {DIR} {SUBDIR_ENV_VALUE}", format_string),
    # ('NULL',),
    ('POSTGRES_ENGINE', 'django.db.backends.postgresql_psycopg2'),
    ('POSTGRES_DB', 'postgres'),
    ('POSTGRES_USER', 'postgres'),
    ('POSTGRES_PASSWORD', 'postgres'),
    ('POSTGRES_HOST', 'db'),
    ('POSTGRES_PORT', ''),
    ('SECRET_KEY', 'secret_key'),
)

ENV_FILES = (
    '.local.env',
    '.env',
)

Config = get_config(DEFAULT_CONFIG, ENV_FILES)
config = Config()

if __name__ == "__main__":
    for key, value in config.items():
        print(f"{key}: {value}")
