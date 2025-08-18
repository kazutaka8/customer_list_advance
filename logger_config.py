# ロガーの練習
import logging


def setup_logger(name, log_file, level=logging.DEBUG):
    # フォーマットを設定（時刻、ロガー名、モジュール名、関数名、行番号、イベントレベル、内容）
    log_format = "%(asctime)s - %(name)s - %(module)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s"

    # ファイルハンドラーの設定（ロガーで取得したイベントをDEBUGレベルまでファイル出力（今回であれば全てになる））
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(log_format))

    # ストリームハンドラーの設定（ロガーで取得したイベントをINFOレベルまでコンソール出力（今回であれば一部になる））
    # console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.INFO)
    # console_handler.setFormatter(logging.Formatter(log_format))

    # peeweeロガーの設定（取得するイベントはDEBUGレベルまで）
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    # logger.addHandler(console_handler)
    logger.setLevel(level)

    return logger
