```

$ curl --form 'from="UniProtKB_AC-ID"' \
     --form 'to="UniProtKB"' \
     --form 'ids="A2Z669,B5ZC00,P07204_TRBM_HUMAN,P20840_SAG1_YEAST"' \
https://rest.uniprot.org/idmapping/run

{"jobId":"73355ca2e443f410d1d73be7856fc5e42e1aa5be"}

$ 
```


```

$ curl -i 'https://rest.uniprot.org/idmapping/status/73355ca2e443f410d1d73be7856fc5e42e1aa5be'

HTTP/2 303
vary: accept,accept-encoding,x-uniprot-release,x-api-deployment-date
vary: User-Agent
cache-control: no-cache
content-type: application/json
access-control-allow-credentials: true
access-control-expose-headers: Link, X-Total-Results, X-UniProt-Release, X-UniProt-Release-Date, X-API-Deployment-Date
x-api-deployment-date: 17-February-2025
strict-transport-security: max-age=31536000; includeSubDomains
date: Tue, 11 Mar 2025 08:48:35 GMT
access-control-max-age: 1728000
x-uniprot-release: 2025_01
location: https://rest.uniprot.org/idmapping/uniprotkb/results/73355ca2e443f410d1d73be7856fc5e42e1aa5be
access-control-allow-origin: *
access-control-allow-methods: GET, PUT, POST, DELETE, PATCH, OPTIONS
access-control-allow-headers: DNT,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type,Range,Authorization
x-uniprot-release-date: 05-February-2025

{"jobStatus":"FINISHED"}

$

```

To get the results use the following command: 

```
# $ curl -s "https://rest.uniprot.org/idmapping/{uniprot_db}/results/{jobId}"
$ curl -s "https://rest.uniprot.org/idmapping/uniprotkb/results/73355ca2e443f410d1d73be7856fc5e42e1aa5be"
```

This downloads the results as a json. 
