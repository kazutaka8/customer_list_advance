# import logger_config
import welcome
import selector

# logger_config.setup_logger("app", "app.log")


def main():
    welcome.welcome_message()
    selector.command_selector()


if __name__ == "__main__":
    main()
