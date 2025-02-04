def validate_sql(data):
    if "SELECT" in data or "FROM" in data or "WHERE" in data or "DROP" in data or "CREATE" in data:
        return False
    else:
        return data