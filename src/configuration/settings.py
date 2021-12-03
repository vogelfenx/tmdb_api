import dotenv

secrets = dotenv.dotenv_values('.secrets', verbose=True)

tmdb_api_key_v3 = secrets['TMDB_API_KEY_V3']
