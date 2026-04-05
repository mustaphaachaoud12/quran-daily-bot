import random
from telegram import Bot
import asyncio
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = 7267064983

# 📖 آيات متوسطة (تقدر تزيد عليهم)
ayat = [
    {
        "text": "يَا أَيُّهَا الَّذِينَ آمَنُوا اصْبِرُوا وَصَابِرُوا وَرَابِطُوا وَاتَّقُوا اللَّهَ لَعَلَّكُمْ تُفْلِحُونَ",
        "tafseer": "أمر بالصبر والثبات والتقوى لتحقيق النجاح."
    },
    {
        "text": "إِنَّ اللَّهَ يَأْمُرُ بِالْعَدْلِ وَالإِحْسَانِ وَإِيتَاءِ ذِي الْقُرْبَىٰ",
        "tafseer": "الله يأمر بالعدل والإحسان ومساعدة الأقارب."
    },
    {
        "text": "وَمَن يَتَّقِ اللَّهَ يَجْعَل لَّهُ مَخْرَجًا وَيَرْزُقْهُ مِنْ حَيْثُ لَا يَحْتَسِبُ",
        "tafseer": "من يخاف الله يفتح له أبواب الرزق والحلول."
    },
    {
        "text": "إِنَّ اللَّهَ لَا يُغَيِّرُ مَا بِقَوْمٍ حَتَّىٰ يُغَيِّرُوا مَا بِأَنفُسِهِمْ",
        "tafseer": "التغيير يبدأ من النفس."
    },
    {
        "text": "فَإِنَّ مَعَ الْعُسْرِ يُسْرًا إِنَّ مَعَ الْعُسْرِ يُسْرًا",
        "tafseer": "بعد الصعوبة يأتي الفرج."
    }
]

# 🎯 اختيار آية بدون تكرار مباشر
last_index = -1

def get_ayah():
    global last_index

    index = random.randint(0, len(ayat) - 1)

    # باش ما تعاودش نفس الآية
    while index == last_index:
        index = random.randint(0, len(ayat) - 1)

    last_index = index

    a = ayat[index]

    return f"""📖 آية اليوم

{a['text']}

📚 التفسير:
{a['tafseer']}

🤍 حاول تحفظها اليوم وعاودها عدة مرات
"""

async def main():
    bot = Bot(token=TOKEN)

    while True:
        try:
            await bot.send_message(chat_id=CHAT_ID, text=get_ayah())
            print("✅ Ayah sent")
        except Exception as e:
            print("❌ Error:", e)

        await asyncio.sleep(86400)

asyncio.run(main())
