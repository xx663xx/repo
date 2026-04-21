from tiny_text_stats import TextStats, analyze_text


def test_analyze_text_counts_regular_text() -> None:
    result = analyze_text("hello world\nagain")

    assert result == TextStats(characters=17, words=3, lines=2)


def test_analyze_text_counts_empty_text() -> None:
    result = analyze_text("")

    assert result == TextStats(characters=0, words=0, lines=0)
