### Run 

* All the containers

    `docker-compose up`

* Message broker 

    `docker-compose -f docker-compose-broker.yml up`

### install Mqtt client

`brew install hivemq/mqtt-cli/mqtt-cli`

* subscribe 
`mqtt sub -t test -h localhost -p 1883`

* publish
` mqtt pub -t test -m "Hello" -h localhost -p 1883`