from rest_framework import serializers


class DriverActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        label="Ação a ser realizada no passageiro",
        choices=(('approve', 'Aprovar'),
                 ('deny', 'Negar'), ('forfeit', 'Remover'))
    )


class FuturePassengerActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        label="Ação a ser realizada na carona",
        choices=(('book', 'Entrar na carona'),)
    )


class PassengerActionsSerializer(serializers.Serializer):
    action = serializers.ChoiceField(
        label="Ação a ser realizada pelo passageiro",
        choices=(('give_up', 'Desistir da carona'),)
    )