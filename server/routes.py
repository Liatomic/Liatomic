from bot_api import account, playing, event_stream, game_stream, bot_abort,\
    bot_resign, bot_chat, bot_move, challenge_accept, challenge_decline,\
    create_bot_seek, challenge_create, bot_pong, bot_analysis
from fishnet import fishnet_monitor, fishnet_key, fishnet_acquire,\
    fishnet_abort, fishnet_analysis, fishnet_move
from game_api import export, get_games, get_user_games, subscribe_games,\
    subscribe_notify, get_variant_stats
from login import login, logout, oauth
from index import index, robots, select_lang
from wsl import lobby_socket_handler
from wsr import round_socket_handler


get_routes = (
    ("/login", login),
    ("/oauth", oauth),
    ("/logout", logout),
    ("/", index),
    ("/about", index),
    ("/faq", index),
    ("/stats", index),
    ("/players", index),
    ("/allplayers", index),
    ("/games", index),
    ("/tv", index),
    ("/analysis/{variant}", index),
    ("/analysis/{variant}/{fen}", index),
    ("/editor/{variant}", index),
    ("/editor/{variant}/{fen}", index),
    (r"/{gameId:\w{8}}", index),
    ("/@/{profileId}", index),
    ("/@/{profileId}/tv", index),
    ("/@/{profileId}/challenge", index),
    ("/@/{profileId}/challenge/{variant}", index),
    ("/@/{profileId}/{variant}", index),
    ("/level8win", index),
    ("/patron", index),
    ("/patron/thanks", index),
    ("/variant", index),
    ("/variant/{variant}", index),
    ("/wsl", lobby_socket_handler),
    ("/wsr", round_socket_handler),
    ("/api/account", account),
    ("/api/account/playing", playing),
    ("/api/stream/event", event_stream),
    ("/api/bot/game/stream/{gameId}", game_stream),
    ("/api/{profileId}/all", get_user_games),
    ("/api/{profileId}/win", get_user_games),
    ("/api/{profileId}/loss", get_user_games),
    ("/api/{profileId}/{variant}", get_user_games),
    ("/api/stats", get_variant_stats),
    ("/api/games", get_games),
    ("/api/ongoing", subscribe_games),
    ("/api/notify", subscribe_notify),
    ("/games/export/{profileId}", export),
    ("/games/export/variant/{variant}", export),
    ("/fishnet/monitor", fishnet_monitor),
    ("/fishnet/key/{key}", fishnet_key),
    ("/robots.txt", robots),
)

post_routes = (
    ("/api/bot/game/{gameId}/abort", bot_abort),
    ("/api/bot/game/{gameId}/resign", bot_resign),
    ("/api/bot/game/{gameId}/analysis", bot_analysis),
    ("/api/bot/game/{gameId}/chat", bot_chat),
    ("/api/bot/game/{gameId}/move/{move}", bot_move),
    ("/api/challenge/{username}", challenge_create),
    ("/api/challenge/{challengeId}/accept", challenge_accept),
    ("/api/challenge/{challengeId}/decline", challenge_decline),
    ("/api/seek", create_bot_seek),
    ("/api/pong", bot_pong),
    ("/fishnet/acquire", fishnet_acquire),
    ("/fishnet/analysis/{workId}", fishnet_analysis),
    ("/fishnet/move/{workId}", fishnet_move),
    ("/fishnet/abort/{workId}", fishnet_abort),
    ("/translation/select", select_lang),
)
