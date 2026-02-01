from services.supabase_client import supabase

def fetch_user_portfolio(user_id):
    response = supabase.table("portfolios") \
        .select("*") \
        .eq("user_id", user_id) \
        .execute()

    return response.data
