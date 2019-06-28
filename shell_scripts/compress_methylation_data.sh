#DIR=/nfs/leia/research/stegle/dseaton/data/retreat_hackathon2019/CompetitionRetreat/MethylationData/Imputed/UDs
DIR=/nfs/leia/research/stegle/dseaton/data/retreat_hackathon2019/CompetitionRetreat/MethylationData/Imputed/D3s
ANNOTATION=/nfs/leia/research/stegle/dseaton/data/retreat_hackathon2019/CompetitionRetreat/Annotation/other-regulatoryFeatures.bed

for f in $DIR/*GRCh38_bismark_bt2.bedGraph.gz; do
    echo $f
    bedtools map -a $ANNOTATION -b $f -c 4 -o mean | gzip --fast > $f.featurecompressed.bed.gz
done
