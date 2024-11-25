import gradio as gr

rules = {
    "o_e_rule": {
        "words": ["чорнозем", "зорепад", "водогін"],
        "explanation": "утворені за допомогою сполучного голосного 'о' або 'е'"
    },
    "hyphen_rule": {
        "words": ["купівля-продаж", "інтернет-магазин", "Вовчик-Братчик", "хліб-сіль"],
        "explanation": "утворені з двох іменників без сполучних голосних"
    },
    "prefix_rule": {
        "words": ["авіарейс", "відеорепортаж", "макроекономіка", "радіопередача", "супершоу"],
        "explanation": "з першою частиною авіа-, аудіо-, агро-, відео-, екстра-, кіно-, мокро-, мікро-, моно-, радіо-, супер-, стерео-"
    },
    "vice_ex_rule": {
        "words": ["віце-ректор", "екс-президент", "максі-програма", "міні-маркет"],
        "explanation": "з першою частиною віце-, екс-, максі-, міні- тощо"
    },
    "measurement_rule": {
        "words": ["тонно-кілометр", "людино-день"],
        "explanation": "назви одиниць виміру"
    },
    "imperative_rule": {
        "words": ["горицвіт", "перекотиполе", "пройдисвіт"],
        "explanation": "утворені з дієслова у формі наказового способу"
    },
    "job_titles_rule": {
        "words": ["прем’єр-міністр", "генерал-майор"],
        "explanation": "назви посад, професій, спеціальностей"
    },
    "numerals_rule": {
        "words": ["п’ятикласник", "сторіччя"],
        "explanation": "з першою частиною, що є числівником"
    },
    "appositions_rule": {
        "words": ["дівчина-красуня", "хлопець-богатир", "дуб-велетень"],
        "explanation": "прикладки, що стоять після пояснюваного іменника"
    },
    "half_rule": {
        "words": ["пів’яблука", "півогірка", "напівавтомат", "полумисок"],
        "explanation": "з першою частиною ні-, напів-, полу-"
    },
    "species_names_rule": {
        "words": ["Дніпро-ріка", "сон-трава", "Ведмідь-гора"],
        "explanation": "видові назви, що стоять перед пояснюваним словом"
    },
    "place_names_rule": {
        "words": ["пів-Києва", "пів-Японії"],
        "explanation": "власні назви з частиною пів-"
    }
}

def check_and_correct_word(word):
    word_found = False
    for rule, data in rules.items():
        correct_forms = data["words"]
        explanation = data["explanation"]

        if word in correct_forms:
            word_found = True
            return f"{word} (правильно: {explanation})"

        if "-" not in word and any(correct_word.replace("-", "") == word for correct_word in correct_forms):
            word_found = True
            correct_word = next(correct_word for correct_word in correct_forms if correct_word.replace("-", "") == word)
            return f"{word} -> {correct_word} (виправлено: {explanation})"

    if not word_found:
        return f"{word} (не знайдено в базі даних)"

    return f"{word} (неправильно або не входить в жодне правило)"

def check_and_correct_text(text):
    if not text.strip():
        return "Помилка: Введений текст порожній. Будь ласка, введіть текст для перевірки."

    words = text.split()
    corrected_words = [check_and_correct_word(word) for word in words]
    return "\n".join(corrected_words)

test_texts = {
    "Тест 1": "відеорепортаж хліб-сіль прем’єр-міністр",
    "Тест 2": "прем’єр-міністр сторіччя віце-ректор",
    "Тест 3": "чорнозем напівавтомат перекотиполе"
}

iface = gr.Interface(
    fn=check_and_correct_text,
    inputs=gr.Textbox(lines=5, placeholder="Введіть текст для перевірки..."),
    outputs=gr.Textbox(lines=10, placeholder="Результат перевірки з'явиться тут..."),
    title="Перевірка написання слів",
    description="Введіть текст для перевірки. Програма перевірить правильність написання слів та вкаже правила.",
    examples=[text for text in test_texts.values()]
)

if __name__ == "__main__":
    iface.launch()
