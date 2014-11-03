# create_imdet.sh

## collect phase and baseline information for science IO
#cp /diska/home/gravmgr/GRAVITY/OS/gvspc/test/calinfo_idx_*.csv data/SC
#dbRead "@wgrav:Appl_data:GRAV:OS:gvspcControl:config.Phases" > SC/data/phases_raw.txt
#dbRead "@wgrav:Appl_data:GRAV:OS:gvspcControl:config.Integrated_optics" > SC/data/IO_raw.txt

## extract x pixels and y pixels from Yitping's configuration files:
for f in `ls calinfo_idx*.csv`; do
	mode=$(echo $f | awk -F "_" '{print $3}' | awk -F "." '{print $1}')
	fx=PX_${mode}.txt
	fy=PY_${mode}.txt
	# line 8 contains the x pixels
	sed -n '8p' $f > $fx
	# lines 12ff contain the y pixels
	tail -n +12 $f > $fy
done
