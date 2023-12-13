## Create
### POST: https://aa4jkqbo36.execute-api.eu-north-1.amazonaws.com/create_user
### Body:{
    full_name:string
    mob_number:string
    pan_number:string
}

## Read
### GET: https://aa4jkqbo36.execute-api.eu-north-1.amazonaws.com/get_users

## Update
### PATCH: https://aa4jkqbo36.execute-api.eu-north-1.amazonaws.com/update_user/{id}
### Body: {
    full_name: string (optional)
    mob_number: string (optional)
    pan_number: string (optional)
}

## Delete
### DELETE: https://aa4jkqbo36.execute-api.eu-north-1.amazonaws.com/delete_user/{id}
