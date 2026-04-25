{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/2321051-maker/korean-ipa-app/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install epitran"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-Va_ign5qd-u",
        "outputId": "451bfc6b-6f67-4863-d62e-5a661e62022b"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting epitran\n",
            "  Downloading epitran-1.35.1-py3-none-any.whl.metadata (36 kB)\n",
            "Requirement already satisfied: regex in /usr/local/lib/python3.12/dist-packages (from epitran) (2025.11.3)\n",
            "Collecting panphon>=0.20 (from epitran)\n",
            "  Downloading panphon-0.22.2-py2.py3-none-any.whl.metadata (15 kB)\n",
            "Collecting marisa-trie (from epitran)\n",
            "  Downloading marisa_trie-1.4.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (10 kB)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.12/dist-packages (from epitran) (2.32.4)\n",
            "Collecting jamo (from epitran)\n",
            "  Downloading jamo-0.4.1-py3-none-any.whl.metadata (2.3 kB)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from panphon>=0.20->epitran) (75.2.0)\n",
            "Collecting unicodecsv (from panphon>=0.20->epitran)\n",
            "  Downloading unicodecsv-0.14.1.tar.gz (10 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Requirement already satisfied: PyYAML in /usr/local/lib/python3.12/dist-packages (from panphon>=0.20->epitran) (6.0.3)\n",
            "Requirement already satisfied: numpy>=1.20.2 in /usr/local/lib/python3.12/dist-packages (from panphon>=0.20->epitran) (2.0.2)\n",
            "Requirement already satisfied: editdistance in /usr/local/lib/python3.12/dist-packages (from panphon>=0.20->epitran) (0.8.1)\n",
            "Collecting munkres (from panphon>=0.20->epitran)\n",
            "  Downloading munkres-1.1.4-py2.py3-none-any.whl.metadata (980 bytes)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.12/dist-packages (from panphon>=0.20->epitran) (2.2.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests->epitran) (3.4.7)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests->epitran) (3.11)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests->epitran) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests->epitran) (2026.2.25)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.12/dist-packages (from pandas->panphon>=0.20->epitran) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas->panphon>=0.20->epitran) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas->panphon>=0.20->epitran) (2026.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil>=2.8.2->pandas->panphon>=0.20->epitran) (1.17.0)\n",
            "Downloading epitran-1.35.1-py3-none-any.whl (221 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m221.3/221.3 kB\u001b[0m \u001b[31m9.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading panphon-0.22.2-py2.py3-none-any.whl (78 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m78.9/78.9 kB\u001b[0m \u001b[31m6.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading jamo-0.4.1-py3-none-any.whl (9.5 kB)\n",
            "Downloading marisa_trie-1.4.1-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (1.5 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.5/1.5 MB\u001b[0m \u001b[31m37.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading munkres-1.1.4-py2.py3-none-any.whl (7.0 kB)\n",
            "Building wheels for collected packages: unicodecsv\n",
            "  Building wheel for unicodecsv (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for unicodecsv: filename=unicodecsv-0.14.1-py3-none-any.whl size=10744 sha256=1a640105d3e417bcd372cf23084876d9f08b9c91043aff4c4693526655eba029\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/67/7d/2e80818c2f3dc8f0735d0810338c47e95d3212114ab97b4ede\n",
            "Successfully built unicodecsv\n",
            "Installing collected packages: unicodecsv, munkres, jamo, marisa-trie, panphon, epitran\n",
            "Successfully installed epitran-1.35.1 jamo-0.4.1 marisa-trie-1.4.1 munkres-1.1.4 panphon-0.22.2 unicodecsv-0.14.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import epitran\n",
        "\n",
        "# 한국어 모델\n",
        "epi = epitran.Epitran('kor-Hang')\n",
        "\n",
        "def to_ipa(text):\n",
        "    return epi.transliterate(text)\n",
        "\n",
        "print(to_ipa(\"안녕하세요\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aY9kxbriqiBy",
        "outputId": "013950f8-7232-4c2d-924b-3f32c561c8c2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "annjʌŋhasejo\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}