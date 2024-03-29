import matplotlib.pyplot as plt
import numpy as np

# podaj nazwy plikow widmowych (.Spe) po przecinku: "Skot pierwiastka"_"liczba atomowa".Spe np V__23.Spe lub V_23_ssdffc-xsnjdn.Spe (wyrazenia po pierwszych 5 znakach nie maja znaczenia)
file_names = [
    # przykladowa nazwa pliku
    "V__23_cw_1.Spe"
]

for file_name in file_names:
    # tabela z wartościami pomiarów, użyta później do wykonania wykresu
    data = []
    # tabela z obszarami pikow
    rois = []

    with open(file_name, "r") as file:
        # ponizsze markery odpowiadaja za zaznaczenie pikow
        start_marker = False
        end_marker = False
        for line in file:
            # zakres kanałów w tym przypadku jest od 0 do 1023, nie musi tak byc!!! Może być zakres np: 0 2047
            # sprawdz w pliku jak jest zapisane, linijka przed wartosciami powinna wygladac w nastepujacy sposob: 0 2^(n)-1
            if line.startswith("0 1023"):
                start_marker = True
                continue

            # szukanie w pliku zapisu o zakresach markerow
            if line.startswith("$ROI:"):
                end_marker = True
                break

            if start_marker and not end_marker:
                data.append(int(line))

    with open(file_name, "r") as file:
        for line in file:
            if line.strip() == "$ROI:":
                num_rois = int(next(file))
                for _ in range(num_rois):
                    roi_start, roi_end = map(int, next(file).split())
                    rois.append((roi_start, roi_end))

    # Wygenerowanie wykresu dla danego pliku
    plt.plot(data)
    plt.title(file_name[:5])
    plt.xlabel("numer kanału")
    plt.ylabel("ilość zliczeń")

    # Zaznaczenie obszarów na wykresie
    for roi in rois:
        roi_start, roi_end = roi
        plt.axvspan(roi_start, roi_end, facecolor="gray", alpha=0.3)

        # Zaznaczenie wartosci w polowie zaznaczonych przedziałow
        mid_point = (roi_start + roi_end) // 2
        plt.axvline(x=mid_point, color="green", linestyle="--")
        plt.text(
            mid_point, max(data), str(mid_point), rotation=0, color="green", ha="right"
        )
        # Obliczenie FWHM
        roi_data = data[roi_start : roi_end + 1]
        half_max = (np.max(roi_data) + np.min(roi_data)) / 2
        indices_above_half_max = np.where(roi_data >= half_max)[0]
        if len(indices_above_half_max) > 0:
            fwhm_start = indices_above_half_max[0]
            fwhm_end = indices_above_half_max[-1]
            fwhm_indices = np.arange(roi_start + fwhm_start, roi_start + fwhm_end + 1)

            # Zaznaczenie wartosci FWHM na wykresie
            plt.text(
                (roi_start + roi_end) / 2,
                half_max,
                f"FWHM:{fwhm_indices[-1]-fwhm_indices[1]}",
                color="red",
                ha="center",
            )
    # Zapis wykresu do pliku JPEG
    plt.savefig(f"{file_name[:5]}.png")
    # wyswietlenie wykresu
    plt.show()
