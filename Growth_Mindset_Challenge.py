{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOuhukgjaH+GrGmn6U3od3M",
      "include_colab_link": True
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sadaqathussain8190/GOV-Sindh-IT-projects-python/blob/main/Growth_Mindset_Challenge_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-9xawaCQkBZw",
        "outputId": "c9068e36-2259-41ac-bc78-8e26dafee358"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Growth Mindset Tracker!\n",
            "What did you learn today? english language\n",
            "What challenge did you face today? words\n",
            "How did you overcome this challenge? yes\n",
            "\n",
            "Motivational Quote for Today:\n",
            "Success is the sum of small efforts, repeated day in and day out. - Robert Collier\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "from datetime import datetime\n",
        "\n",
        "quotes = [\n",
        "    \"The only way to do great work is to love what you do. - Steve Jobs\",\n",
        "    \"Success is the sum of small efforts, repeated day in and day out. - Robert Collier\",\n",
        "    \"It does not matter how slowly you go as long as you do not stop. - Confucius\"\n",
        "]\n",
        "\n",
        "def track_progress():\n",
        "    today = datetime.today().strftime('%Y-%m-%d')\n",
        "\n",
        "    learning = input(\"What did you learn today? \")\n",
        "    challenge = input(\"What challenge did you face today? \")\n",
        "    reflection = input(\"How did you overcome this challenge? \")\n",
        "\n",
        "    with open(\"growth_mindset_tracker.txt\", \"a\") as file:\n",
        "        file.write(f\"{today}, {learning}, {challenge}, {reflection}\\n\")\n",
        "\n",
        "    print(\"\\nMotivational Quote for Today:\")\n",
        "    print(random.choice(quotes))\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    print(\"Welcome to the Growth Mindset Tracker!\")\n",
        "    track_progress()\n",
        "\n"
      ]
    }
  ]
}
