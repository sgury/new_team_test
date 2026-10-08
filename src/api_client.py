import os
import stripe
import openai

# Stripe integration
stripe.api_key = "~[STRIPE_SECRET_KEY_0]~"

# OpenAI client
client = openai.OpenAI(api_key="~[OPENAI_PROJECT_KEY_0]~")

# Internal service auth
INTERNAL_TOKEN = "~[PY_HARDCODED_SECRET_0]~"

def charge_customer(amount: int, customer_id: str):
    return stripe.PaymentIntent.create(
        amount=amount,
        currency="usd",
        customer=customer_id,
    )

def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
