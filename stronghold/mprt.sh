#!/usr/bin/bash

# change the ids below

curl --request POST 'https://rest.uniprot.org/idmapping/run' --form 'ids="P21802,P12345"' --form 'from="UniProtKB_AC-ID"' --form 'to="UniRef90"'

# output to terminal
# {"jobId":"27a020f6334184c4eb382111fbcad0e848f40300"}

# check the status of job
# $ curl -i 'https://rest.uniprot.org/idmapping/status/27a020f6334184c4eb382111fbcad0e848f40300'

# get results of job from: 
# GET /idmapping/results/{jobId}
# or
# GET /idmapping/{uniprot_db}/results/{jobId} ## where {uniprot_db} is one of UniParc, UniProtKB or UniRef
#
# $ curl -s "https://rest.uniprot.org/idmapping/uniref/results/27a020f6334184c4eb382111fbcad0e848f40300"
