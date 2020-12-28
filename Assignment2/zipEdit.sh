echo "Usage: zipedit filename.gz filename.txt"
unzip "$1" "$2" -d /tmp
echo "sed -i /tmp/"$2" && zip -j --update "$1" "/tmp/$2""
