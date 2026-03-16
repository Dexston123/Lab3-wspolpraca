from pydantic import BaseModel
from typing import Dict, List
from src.models import Parameters
from src.manager import Manager

import json



if __name__ == '__main__':
    parameters = Parameters()
    manager = Manager(parameters)

    print("=" * 50)
    print("🏢 RAPORT ZARZĄDCY NIERUCHOMOŚCI")
    print("=" * 50)

    print("\n--- MIESZKANIA ---")
    for apartment in manager.apartments.values():
        print(f"\n🏠 Mieszkanie: {apartment.name} ({apartment.key})")
        print(f"   Lokalizacja: {apartment.location} | Powierzchnia: {apartment.area_m2} m2")
        
        print("   Pokoje:")
        for room in apartment.rooms.values():
            print(f"     - {room.name} ({room.area_m2} m2)")
        
        print("   Rachunki:")
        has_bills = False
        for bill in manager.bills:
            if bill.apartment == apartment.key:
                has_bills = True
                print(f"     * [{bill.date_due}] {bill.type.capitalize()}: {bill.amount_pln} PLN (Okres: {bill.settlement_month}/{bill.settlement_year})")
        if not has_bills:
            print("     * Brak rachunków")

    print("\n" + "-" * 50)
    print("--- NAJEMCY ---")
    for tenant in manager.tenants.values():
        print(f"\n👤 Najemca: {tenant.name}")
        print(f"   Lokal: {tenant.apartment}, Pokój: {tenant.room}")
        print(f"   Umowa: {tenant.date_agreement_from} do {tenant.date_agreement_to} | Czynsz: {tenant.rent_pln} PLN | Kaucja: {tenant.deposit_pln} PLN")
        
        print("   Przelewy:")
        has_transfers = False
        for transfer in manager.transfers:
            if transfer.tenant == tenant.name:
                has_transfers = True
                miesiac = transfer.settlement_month if transfer.settlement_month else 'N/A'
                rok = transfer.settlement_year if transfer.settlement_year else 'N/A'
                print(f"     * [{transfer.date}] Wpłata: {transfer.amount_pln} PLN (Za: {miesiac}/{rok})")
        if not has_transfers:
            print("     * Brak wpłat")
            
    print("\n" + "=" * 50)
