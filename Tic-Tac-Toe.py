{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e180ad2c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def sum(a,b,c):\n",
    "    return a + b + c\n",
    "def printboard(xstate,zstate):\n",
    "    zero='X' if xstate[0] else (\"O\" if zstate[0] else 0)\n",
    "    one='X' if xstate[1] else (\"O\" if zstate[1] else 1)\n",
    "    two='X' if xstate[2] else (\"O\" if zstate[2] else 2)\n",
    "    three='X' if xstate[3] else (\"O\" if zstate[3] else 3)\n",
    "    four='X' if xstate[4] else (\"O\" if zstate[4] else 4)\n",
    "    five='X' if xstate[5] else (\"O\" if zstate[5] else 5)\n",
    "    six='X' if xstate[6] else (\"O\" if zstate[6] else 6)\n",
    "    seven='X' if xstate[7] else (\"O\" if zstate[7] else 7)\n",
    "    eight='X' if xstate[8] else (\"O\" if zstate[8] else 8)\n",
    "    print(f\"{zero} | {one} | {two} \")\n",
    "    print(f\"--|---|---\")\n",
    "    print(f\"{three} | {four} | {five} \")\n",
    "    print(f\"--|---|---\")\n",
    "    print(f\"{six} | {seven} | {eight} \")\n",
    "    \n",
    "def checkWin(xstate,zstate):\n",
    "    wins =[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]\n",
    "    for win in wins:\n",
    "        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):\n",
    "            print(\"X won the match!\")\n",
    "            return 1\n",
    "        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):\n",
    "            print(\"O won the match!\")\n",
    "            return 0\n",
    "    return -1  \n",
    "\n",
    "        \n",
    "    \n",
    "if __name__==\"__main__\":\n",
    "    xstate = [0,0,0,0,0,0,0,0,0]\n",
    "    zstate = [0,0,0,0,0,0,0,0,0]\n",
    "    turn=1 #1 for X and 0 for O\n",
    "    print(\"Welcome to tic tac toe\")\n",
    "    while (True):\n",
    "        printboard(xstate,zstate)\n",
    "        if(turn == 1):\n",
    "             print(\"X's Chance\")\n",
    "             value =int(input(\"Enter A Value: \"))\n",
    "             xstate[value]=1\n",
    "        else:\n",
    "            print(\"O's Chance\")\n",
    "            value=int(input(\"Enter a Value: \"))\n",
    "            zstate[value]=1\n",
    "        cwin= checkWin(xstate,zstate)\n",
    "        if (cwin !=-1):\n",
    "            print(\"Match over\")\n",
    "            break\n",
    "        turn=1-turn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "345e5997",
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
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
