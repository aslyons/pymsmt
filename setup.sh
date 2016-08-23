for dir in api mcpb lib msmtmol ipmach
do
/bin/cp -LR $dir $1/
done

/bin/cp pymsmtexp.py $1/
/bin/cp title.py $1/

for prog in CartHess2FC.py espgen.py MCPB.py PdbSearcher.py car2mol2.py
do
sed '1c#!'$2'' msmttools/$prog > $1/$prog
chmod +x $1/$prog
done
