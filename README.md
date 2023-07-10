Tech by Kenzie Store

Este projeto é uma API para suportar uma plataforma de e-commerce chamada Tech by Kenzie Store. A plataforma permite que usuários realizem compras, adicionem produtos ao carrinho, finalizem pedidos e muito mais.

Funcionalidades:

Produtos
Os usuários podem buscar produtos por nome, categoria e ID.
Os produtos possuem um campo de estoque que indica a disponibilidade do produto.
Se um produto estiver com 0 unidades em estoque, ele é considerado indisponível.
Ao finalizar a compra, se um produto estiver indisponível, um erro será retornado.
A criação de um pedido deve subtrair a quantidade dos produtos do estoque.

Carrinho
Os usuários podem adicionar produtos ao carrinho antes de finalizar a compra.
O carrinho contém uma lista dos produtos selecionados, juntamente com seus valores.
Um pedido não pode ser finalizado se não houver estoque dos produtos.
Se os produtos no carrinho forem de diferentes vendedores, um pedido separado será criado para cada vendedor.

Pedido
Cada pedido possui um status: PEDIDO REALIZADO, EM ANDAMENTO ou ENTREGUE.
Sempre que o status de um pedido for atualizado, um e-mail será enviado ao comprador.
Os pedidos contêm todos os dados dos produtos, exceto a quantidade em estoque.
O vendedor do produto pode atualizar o status do pedido.
O pedido contém o horário em que foi feito.

Endereço
Os usuários têm um relacionamento com um campo de endereço.
Os clientes podem cadastrar múltiplos endereços de entrega e configurar um deles como padrão.

Usuários
O sistema permite o cadastro de usuários com diferentes níveis de acesso:

Administrador
Vendedor
Cliente

Usuários não autenticados podem acessar a plataforma para visualizar informações sobre os produtos.
Funcionalidades específicas são permitidas para cada tipo de usuário.
Funcionalidades por Tipo de Usuário

Administrador
O administrador pode transformar um usuário comum em vendedor.
O usuário administrador tem acesso a todas as rotas.

Vendedor
O vendedor pode cadastrar novos produtos na plataforma.
O vendedor pode atualizar o estoque do produto.
O vendedor pode verificar os pedidos realizados.
O vendedor tem todos os acessos de um cliente.

Cliente
O cliente pode atualizar o perfil para se tornar vendedor.
O cliente pode adicionar produtos ao carrinho.
O cliente pode finalizar a compra dos produtos.
O cliente pode visualizar todos os pedidos comprados.
