for f in presplit/tw_*.json
do
    echo $f
    cat $f | python data_pp.py | python filter_tw.py > ${f%.json}.tsv
done
