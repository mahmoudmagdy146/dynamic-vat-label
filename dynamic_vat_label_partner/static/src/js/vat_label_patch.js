import { patch } from "@web/core/utils/patch";
import { FormRenderer } from "@web/views/form/form_renderer";
import { onMounted, onPatched } from "@odoo/owl";
import { _t } from "@web/core/l10n/translation";

patch(FormRenderer.prototype, {

    setup() {
        super.setup();

        // Run when component is mounted
        onMounted(() => {
            this._updateVatLabel();
        });

        // Run every time UI updates (important for reactivity)
        onPatched(() => {
            this._updateVatLabel();
        });
    },

    _updateVatLabel() {
        try {
            const record = this.props.record;

            // ✅ Limit to res.partner only
            if (!record || record.resModel !== "res.partner") {
                return;
            }

            const personType = record.data.person_type;
            console.log("Model:", record.resModel);
            console.log("Person Type:", personType);

            let label = _t("Passport ID");
            if (personType === "B") {
                label = "Tax ID";
            } else if (personType === "P") {
                label = "National ID";
            }

            // 🔹 placeholder (👈 هنا تحط الكود بتاعك)
            let placeholder = label;

            if (personType === "B") {
                placeholder = "Registration Number / VAT Number";
            } else if (personType === "P") {
                placeholder = "National ID";
            } else {
                placeholder = "Passport ID";
            }

            // 🎯 1. Update label
            const labelEl = document.querySelector("label[for='vat_0']") || document.querySelector("label[for='vat_1']") || document.querySelector("label[for='vat_2']");

            if (labelEl) {
                labelEl.textContent = label;
            }

            // 🎯 2. Update input placeholder
            const input = document.querySelector("input[id='vat_0']") || document.querySelector("input[id='vat_1']") || document.querySelector("input[id='vat_2']");
            if (input) {
                input.placeholder = placeholder;
            }
            console.log("LABEL:", labelEl,input);

        } catch (error) {
            console.warn("VAT label patch error:", error);
        }
    },
});