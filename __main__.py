import pulumi
import pulumi_aws as aws

# Crear grupo de seguridad para puertos 22 y 80
sec_group = aws.ec2.SecurityGroup("web-secgroup",
    description="Allow SSH and HTTP",
    ingress=[
        {"protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"]},
        {"protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"]}
    ],
    egress=[
        {"protocol": "-1", "from_port": 0, "to_port": 0, "cidr_blocks": ["0.0.0.0/0"]}
    ]
)

# Crear la instancia EC2
ec2_instance = aws.ec2.Instance("cloud9-ec2",
    instance_type="t2.micro",
    ami="ami-043cbf1cf918dd74f",
    key_name="vockey",
    vpc_security_group_ids=[sec_group.id],
    root_block_device={
        "volume_size": 20
    },
    tags={
        "Name": "Nuevo_EC2"
    }
)