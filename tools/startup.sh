/usr/bin/pkill -9 python # kill all python processes todo - make this more specific
/usr/bin/tmux new-session -d -s ENTER
/usr/bin/tmux detach -s ENTER
sleep 3
/usr/bin/tmux send-keys -t 0 "python ~/notion_assistant/notion_assistant/jarvis/jarvis.py" ENTER
echo "$(date) ${1} RESTARTED Jarvis"