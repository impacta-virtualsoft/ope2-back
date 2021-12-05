from rest_framework import exceptions, serializers, pagination

from backend.core.models import Client, Provider, Address

class SmallResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class AddressSerializer(serializers.ModelSerializer):
    pagination_class = SmallResultsSetPagination
    class Meta:
        model = Address
        fields = ["cep", "logradouro", "complemento",
                  "bairro", "localidade", "uf"]


class ClientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)
    pagination_class = SmallResultsSetPagination
    class Meta:
        model = Client
        fields = ["id", "cpf", "name", "address"]

    def create(self, validated_data):
        address = validated_data.get("address", "")

        if address:
            address_dict = {
                "cep": address.get('cep', ''),
                "logradouro": address.get('logradouro', ''),
                "complemento": address.get('complemento', ''),
                "bairro": address.get('bairro', ''),
                "localidade": address.get('localidade', ''),
                "uf": address.get('uf', ''),
            }

            fk_address = Address.objects.create(**address_dict)
        if fk_address:
            client_dict = {
                "cpf": validated_data.get("cpf", ""),
                "name": validated_data.get("name", ""),
                "address": fk_address
            }
            client = Client.objects.create(**client_dict)
        else:
            client_dict = {
                "cpf": validated_data.get("cpf", ""),
                "name": validated_data.get("name", ""),
                "address": ""
            }
            client = Client.objects.create(**client_dict)

        validated_data["id"] = client.id

        return validated_data

    def update(self, instance, validated_data):
        address = validated_data.get(
            "address", instance.address
        )

        if address != instance.address:
            instance.address.cep = address.get('cep', '') if address.get('cep', '') else instance.address.cep
            instance.address.logradouro = address.get('logradouro', '') if address.get('logradouro', '') else instance.address.logradouro
            instance.address.complemento = address.get('complemento', '') if address.get('complemento', '') else instance.address.complemento
            instance.address.bairro = address.get('bairro', '') if address.get('bairro', '') else instance.address.bairro
            instance.address.localidade = address.get('localidade', '') if address.get('localidade', '') else instance.address.localidade
            instance.address.uf = address.get('uf', '') if address.get('uf', '') else instance.address.uf

            instance.address.save()

        instance.cpf = validated_data.get("cpf", '') if validated_data.get("cpf", '') else  instance.cpf
        instance.name = validated_data.get("name", '') if validated_data.get("name", '') else  instance.name
        instance.save()

        return instance


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = "__all__"
