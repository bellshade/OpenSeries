import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import NextTopLoader from "nextjs-toploader";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
    title: "OpenSeries",
    description:
        "Project Untuk Menghitung Segala Jenis Persamaan atau Rumus-Rumus yang terdapat pada bangku sekolah (SMA/SMK/Sederajat). Project ini bertujuan untuk memudahkan siswa dalam menghitung persamaan atau problem-problem yang terdapat pada pelajaran sekolah (cheat egine untuk Sekolah)."
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
    return (
        <html lang="en">
            <body className={`${inter.className} bg-zinc-200`}>
                <NextTopLoader color="#27272a" />
                {children}
            </body>
        </html>
    );
}
