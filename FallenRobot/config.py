class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20539290
    API_HASH = "26e0c15a6803997a3e58d564be36f8f3"

    CASH_API_KEY = "2ATSJ753CLE402MQ"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://neondb_owner:npg_FueRAIz48ZaS@ep-solitary-haze-a8lylhhz-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = -1002124344872  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb://mongo:SKfqQfOojkSyZmLRhxufNMjbyQPgWTFW@nozomi.proxy.rlwy.net:52328"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://vault.pictures/p/08641f944b7b45ee90634dc44e2f85d4"

    SUPPORT_CHAT = GARUD_SUPPORT  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = 6821828314:AAES-su9N9iQrQ4LtD5BWClzJX2jfdfxkns""  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "9LMMJQ30GM49"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7448520005  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
