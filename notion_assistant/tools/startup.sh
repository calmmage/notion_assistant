/usr/bin/pkill -9 python # kill all python processes todo - make this more specific
/usr/bin/tmux new-session -d -s ENTER
/usr/bin/tmux detach -s ENTER
sleep 3
/usr/bin/tmux send-keys -t 0 "cd ~/notion_assistant;dev/jarvis_app.py" ENTER # todo move jarvis_app to notion_assistant folder
echo "$(date) ${1} RESTARTED Jarvis"