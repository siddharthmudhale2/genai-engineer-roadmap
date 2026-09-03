import asyncio


async def stream_words(
    text: str
):

    for word in text.split():

        yield word

        await asyncio.sleep(0.2)