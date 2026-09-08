from model import model_lead
import control


def add_leads():
    name = input("Nome: ").strip()
    email = input("Email: ").strip()
    stage = input("Stage: ").strip()
    company = input("Company: ").strip()

    # Validação executada ANTES da confirmação
    if not name or not email or "@" not in email:
        print("Nome e e-mail válido são obrigatórios.")
        return

    # Criação do objeto lead
    lead_data = model_lead(name, email, company, stage)
    control.create_leads(lead_data)

    print("Lead adicionado com sucesso!")


def list_leads():
    leads = control.read_leads()
    if not leads:
        print("Nenhum lead encontrado.")
        return

    print("\n#  | NOME                | EMPRESA              | EMAIL")
    # Singular 'lead' para não sobrescrever a lista 'leads'
    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead['nome']:<19} | {lead['company']:<20} | {lead['email']:<20}")


def main():
    while True:
        print("\nMini CRM - 1ª aula - (adicionar/listar)")
        print("[1] Adicionar lead")
        print("[2] Listar leads")
        print("[0] Sair do programa")

        opt = input("Escolha uma ação: ").strip()
        if opt == "1":
            add_leads()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
