import data_scrape
import voice_handler

engine = voice_handler.init_engine()
voice = voice_handler.get_voice(engine)
voice_handler.speak('Choose food', voice, engine)
food = voice_handler.get_audio()
print(food)
voice_handler.speak('How many grams?', voice, engine)
amount = voice_handler.get_audio()
print(amount)

data_scrape.log_calories(food + ' calories', float(amount))
