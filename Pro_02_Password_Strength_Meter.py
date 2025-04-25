{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM4xaLDjtjJ+zHbKUiEDbc7",
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
        "<a href=\"https://colab.research.google.com/github/sadaqathussain8190/-GOV-Sindh-IT-project1-Resume-Builder-/blob/main/Pro_02_Password_Strength_Meter.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "id": "eQLVIPHQ_9iN",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "83d943f9-f5e4-435f-a5dc-e473c32d625d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your password:Sadaqat@123\n",
            "Password is strong\n"
          ]
        }
      ],
      "source": [
        "import re\n",
        "password = input(\"Enter your password:\")\n",
        "if  len(password) < 8:\n",
        "  print(\"Password must be at least 8 characters long. \")\n",
        "elif not re.search(\"[A-Z]\" , password):\n",
        "  print(\"Password must contain at least one uppercase letter.\")\n",
        "elif not re.search(\"[a-z]\",password):\n",
        "  print(\"Password must contain at least one lowercase letter.\")\n",
        "elif not re.search(\"[0-9]\",password):\n",
        "  print(\"Password must contain at least one number.\")\n",
        "elif not re.search(\"[@]\",password):\n",
        "  print(\"Password must contain at least one special character (@).\")\n",
        "else:\n",
        "  print(\"Password is strong\")"
      ]
    }
  ]
}
