"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import React, { Fragment } from "react";

type Props = {};

const links = {
    "Get Started": [
        {
            title: "Tentang",
            href: "/docs",
        },
        {
            title: "Instalasi",
            href: "/docs/get-started/instalasi",
        },
    ],
    Matematika: [
        {
            title: "Radian ke derajat",
            href: "/docs/matematika/radian-ke-derajat",
        },
        {
            title: "Luas Lingkaran",
            href: "/docs/matematika/luas-lingkaran",
        },
        {
            title: "Keliling Lingkaran",
            href: "/docs/matematika/keliling-lingkaran",
        },
        {
            title: "Diameter Lingkaran",
            href: "/docs/matematika/diameter-lingkaran",
        },
        {
            title: "Persamaan Kuadrat",
            href: "/docs/matematika/persamaan-kuadrat",
        },
    ],
};

export default function Sidebar({}: Props) {
    const pathname = usePathname();

    return (
        <aside className="flex min-w-[250px] max-w-[250px] grow flex-col gap-4 overflow-y-auto border-r p-6">
            {Object.keys(links).map((category) => (
                <Fragment key={category}>
                    {!!category && <span className="text-xs font-bold uppercase text-zinc-400">{category}</span>}
                    <div className="flex flex-col">
                        {links[category].map((link) => (
                            <Link
                                key={link.href}
                                className={`border-l-2 py-2 pl-6 text-sm ${link.href === pathname ? "border-l-zinc-800 text-zinc-800" : "text-zinc-400"}`}
                                href={link.href}
                            >
                                {link.title}
                            </Link>
                        ))}
                    </div>
                </Fragment>
            ))}
        </aside>
    );
}
