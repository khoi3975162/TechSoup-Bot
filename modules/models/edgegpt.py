import re
from EdgeGPT import Chatbot, ConversationStyle

bot = Chatbot(cookie_path=os.path.dirname('./cookies.json'))


async def run(prompt: str) -> str:
    """
    This is an async function that takes a prompt as input, sends it to a bot, and returns the bot's
    response along with additional information.

    :param prompt: The prompt is the message or question that the bot will ask the user. It is the input
    that the user provides to the bot
    :type prompt: str
    :return: The function `run` returns a tuple containing two values: `text` and `learn_more`.
    """
    # ask bot until response is available (check if the message trying to get is the last limit)
    while True:
        try:
            response = await bot.ask(
                prompt=prompt, conversation_style=ConversationStyle.creative)
            if response["item"]["firstNewMessageIndex"] == None:
                await bot.reset()
                continue
            break
        except:
            continue

    # reset if reaching limit
    capped = False
    if response["item"]["messages"][1]["contentOrigin"] == "TurnLimiter":
        capped = True
        await bot.reset()
        response = await bot.ask(
            prompt=prompt, conversation_style=ConversationStyle.creative)

    try:
        # filter [0], [1], [2], ... out of message
        msg_text = filter_msg_text(response)

        # trip learn more
        learn_more = get_lm_sr(
            response, msg_text
        )
    except KeyError:
        msg_text = response["item"]["messages"][1]["adaptiveCards"][0]["body"][0][
            "text"
        ]
        learn_more = ""

    # set when reset limit notice
    if capped:
        text = "The max number of messages in the previous conversation has been reached, the response below is in the new conversation\n\n" + msg_text
    else:
        text = msg_text

    return text, learn_more


def filter_msg_text(response):
    """
    This function filters and modifies a message text by removing certain characters and replacing them
    with their original form.

    :param response: The response parameter is expected to be a dictionary object containing information
    about a message, such as its text content and metadata
    :return: The function `filter_msg_text` returns the modified message text obtained from the input
    `response` parameter. The modified message text is obtained by removing the `^` character from any
    substring enclosed in square brackets `[]` that matches the regular expression pattern
    `\[([0-9^]+)\]`. If the input `response` parameter does not contain the expected structure, a
    `KeyError`
    """
    try:
        msg_text = response["item"]["messages"][1]["text"]
    except KeyError:
        raise KeyError
    mark_matches = re.findall(r"\[([0-9^]+)\]", msg_text, re.DOTALL)
    for match in mark_matches:
        msg_text = msg_text.replace(match, match.replace("^", ""))
    return msg_text


def get_lm_sr(response, msg_text):
    """
    The function extracts a "Learn more" message from a response object and returns it as a string.

    :param response: It is a dictionary object that contains the response received from an API or a
    server. It may contain various information such as status code, headers, and message body
    :param msg_text: It is a string variable that contains the text of the message sent by the user
    :return: a string that contains information about how to learn more about a certain topic. The
    string is extracted from a JSON response and formatted to include links to additional resources.
    """
    learn_more = ""
    try:
        learn_more = (
            response["item"]["messages"][1]["adaptiveCards"][0]["body"][1]["text"]
            .replace("Learn more: ", "")
            .replace(") [", ")\n[")
        )
    except:
        pass
    return learn_more
