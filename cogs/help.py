import disnake
from disnake.ext import commands
from func import *
import json


class helpc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot = load_json("premium.json")


    @commands.slash_command(name="help", description="Помощь по командам.")
    async def __help(self, ctx):
        view = design_help_cmd()
        embed = disnake.Embed(title=f'**__Список команд__**', description='Пожалуйста, выберите категорию.', color = disnake.Color.green())
        embed.set_footer(text = f"Запросил команду: {ctx.author.name}")
        await ctx.send(embed=embed, view=view)


class design_help_cmd(disnake.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(help_cmd())

class help_cmd(disnake.ui.Select):
    def __init__(self):
        options = [
            disnake.SelectOption(label='Развлечения', description='Куча весёлостей и развлечений!', emoji='<:fun:1004671040116490300>'),
            disnake.SelectOption(label='Модерация', description='Команды для модераторов / Администрации.', emoji='<:moderator:1004670538758754445>'),
            disnake.SelectOption(label='Глобальный чат', description='Общение с разнами серверами через бота.', emoji='<:chat:992097506748010656>'),
            disnake.SelectOption(label='Общее', description='Общие команды для обычных юзеров.', emoji='<:all:1004659237336657972>'),
            disnake.SelectOption(label='Животные', description='Изображение животных.', emoji='<:animals:1004669831217422417>'),
            disnake.SelectOption(label='NSFW', description='18+ изображение', emoji='<:18:1004669364705955852>'),
            disnake.SelectOption(label='Информация', description='Полезные команды', emoji='<:info:992096997500780574>'),
            disnake.SelectOption(label='Premium', description='Покупка подписки', emoji='💲'),
        ]
        super().__init__(placeholder='Выбор категории', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: disnake.Interaction):
        if "Развлечения" in self.values:
            embed = disnake.Embed(color=disnake.Color.yellow())
            embed.add_field(name='Развлечения', value=f'`/test` > Проверка бота\n`/emojify` > Текст из эмодзи как у Dank Memer\n`/gay` > Проверка на гея\n`/meme` > Мем к сожеление на англиском\n`/natural` > Показывает на сколько вы натурал\n`/iq` > Ваш IQ')
            await interaction.response.edit_message(embed=embed)
        if "Модерация" in self.values:
            embed = disnake.Embed(color=disnake.Color.blurple())
            embed.add_field(name='Модерация', value=f'`/clear` > Очистка чата\n`/embed` > Эмбед от имени бота\n`/poll` > Голосование')
            await interaction.response.edit_message(embed=embed)
        if "Глобальный чат" in self.values:
            embed = disnake.Embed(color=disnake.Color.purple())
            embed.add_field(name='Глобальный чат', value=f'`n.global-set` > Установить глобальный чат\n`n.global-remove` > Удалить глобальный чат')
            await interaction.response.edit_message(embed=embed)
        if "Общее" in self.values:
            embed = disnake.Embed(color=disnake.Color.blue())
            embed.add_field(name='Общее', value=f'`/top-guilds` > Топ гильдии по участника\n`/server-info` > Информация о сервере\n`/send-dm` > Отправить сообщение кому-то в ЛС')
            await interaction.response.edit_message(embed=embed)
        if "Животные" in self.values:
            embed = disnake.Embed(color=disnake.Color.green())
            embed.add_field(name='Животные', value=f'`/dog` > Собака\n`/cat` > Кот\n`/fox` > Лиса\n`/koala` > Коала\n`/red-panda` > Красная панда\n`/panda` > Панда\n`/birb` > Бибр')
            await interaction.response.edit_message(embed=embed)
        if "NSFW" in self.values:
            embed = disnake.Embed(color=disnake.Color.red())
            embed.add_field(name='NSFW', value=f'`/waifu`\n`/blowjob`\n`/trap`\n`/neko`\n`/solo`\n`/sex`')
            await interaction.response.edit_message(embed=embed)
        if "Информация" in self.values:
            embed = disnake.Embed(color=disnake.Color.green())
            embed.add_field(name="Информация", value=f"`/support` > Поддержка бота\n`/invite` > Пригласить бота на свой сервер\n`/bot` > Информация о боте\n`/news` > Новости бота\n`/youtube-channel` > Наш личный ютуб канал")
            await interaction.response.edit_message(embed=embed)
        if "Premium" in self.values:
            embed = disnake.Embed(color = disnake.Color.dark_theme())
            embed.add_field(name="Premium", value="`/premium` > Информация о подписке\n`/buy-premium` > Купить подписку")
            await interaction.response.edit_message(embed=embed)

def setup(bot):
    bot.add_cog(helpc(bot))