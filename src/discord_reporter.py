from discord_webhook import DiscordWebhook

from config import (
    DISCORD_WEBHOOK_URL
)


def send_summary(message):

    webhook = DiscordWebhook(
        url=DISCORD_WEBHOOK_URL,
        content=message
    )

    response = webhook.execute()

    return response