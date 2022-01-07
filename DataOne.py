{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "50138703",
   "metadata": {},
   "source": [
    "## Listas e Extruturas de Dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e12ce6c7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "c50fe023",
   "metadata": {},
   "outputs": [],
   "source": [
    "#List with many elements.\n",
    "ShoppingListOne = [\"Mouse Razer\",\"Magic keyboard\",\"iphone13\",\"headset Razer\"]\n",
    "\n",
    "#List with only one element.\n",
    "ShoppingListTwo = [\"Magic Mouse, keyboard Razer, airPods, RazerPhone\"]\n",
    "\n",
    "#list of lists\n",
    "ShoppingListTree = [[\"Mouse1k\",\"Mouse2k\"],[\"keyboard,keyboardTwo\"],[\"iphone13\",\"iphone6s\"],[\"RazerPhone\"]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "id": "bd812897",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mouse1k\n"
     ]
    }
   ],
   "source": [
    "Phone_Apple = ShoppingListOne[2]\n",
    "MouseList   = ShoppingListTree[0]\n",
    "Mouse       = MouseList[0]\n",
    "print(Mouse1k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "5e46df29",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0\n",
      "True\n",
      "iphone6s\n"
     ]
    }
   ],
   "source": [
    "Phone = ShoppingListTree[2][1]\n",
    "number = 'iphone6s' in ShoppingListTree[2][1]\n",
    "\n",
    "print(ShoppingListTree.count(\"iphone6s\"))\n",
    "print(number)\n",
    "print(Phone)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "75234eb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['Mouse1k', 'Mouse2k'], ['keyboard,keyboardTwo'], ['iphone13', 'iphone6s'], ['RazerPhone'], ['Galaxy Tab', 'Ipad mini']]\n"
     ]
    }
   ],
   "source": [
    "NewItem = [\"Galaxy Tab\",\"Ipad mini\"]\n",
    "ShoppingListTree.append(NewItem)\n",
    "print(ShoppingListTree)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "id": "74374010",
   "metadata": {},
   "outputs": [],
   "source": [
    "#copying a list\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d60940fb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec7e358a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
